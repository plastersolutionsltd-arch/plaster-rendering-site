/**
 * Service Worker - Caching Strategy for Performance
 * Implements cache-first strategy for assets, network-first for HTML
 */

const CACHE_NAME = 'plaster-v2';
const ASSETS_CACHE = 'plaster-assets-v2';

// Assets to cache on install
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/vercel.json'
];

// Install event - cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    }).catch(err => {
      console.log('Install cache error:', err);
    })
  );
  self.skipWaiting();
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cacheName) => {
          if (cacheName !== CACHE_NAME && cacheName !== ASSETS_CACHE) {
            return caches.delete(cacheName);
          }
        })
      );
    })
  );
  self.clients.claim();
});

// Fetch event - implement caching strategy
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  // Skip cross-origin requests and chrome extensions
  if (url.origin !== location.origin) {
    return;
  }

  // Network-first strategy for HTML documents
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          if (response.ok) {
            const cache = caches.open(CACHE_NAME);
            cache.then((c) => c.put(request, response.clone()));
          }
          return response;
        })
        .catch(() => {
          return caches.match(request) || caches.match('/index.html');
        })
    );
    return;
  }

  // Cache-first strategy for images, CSS, JS
  if (
    url.pathname.match(/\.(js|css|webp|jpeg|jpg|png|gif|svg|woff|woff2|ttf)$/i)
  ) {
    event.respondWith(
      caches.match(request).then((cached) => {
        return (
          cached ||
          fetch(request).then((response) => {
            if (response.ok) {
              caches.open(ASSETS_CACHE).then((cache) => {
                cache.put(request, response.clone());
              });
            }
            return response;
          }).catch(() => {
            // Return placeholder for images if offline
            if (request.destination === 'image') {
              return new Response(
                `<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
                  <rect fill="#f0f0f0" width="100" height="100"/>
                  <text x="50" y="50" text-anchor="middle" font-family="Arial" font-size="14" fill="#999">offline</text>
                </svg>`,
                {
                  headers: { 'Content-Type': 'image/svg+xml' },
                }
              );
            }
            return null;
          })
        );
      })
    );
    return;
  }

  // Default network-first for other requests
  event.respondWith(
    fetch(request).catch(() => {
      return caches.match(request);
    })
  );
});

// Handle messages from clients
self.addEventListener('message', (event) => {
  if (event.data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  }
});
