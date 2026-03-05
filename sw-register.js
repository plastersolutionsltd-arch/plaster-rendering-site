/**
 * Service Worker Registration
 * Safely registers the service worker with fallback
 */

if ('serviceWorker' in navigator && location.protocol === 'https:') {
  window.addEventListener('load', async () => {
    try {
      const registration = await navigator.serviceWorker.register('/service-worker.js', {
        scope: '/'
      });

      console.log('Service Worker registered:', registration);

      // Listen for updates
      registration.addEventListener('updatefound', () => {
        const newWorker = registration.installing;
        newWorker.addEventListener('statechange', () => {
          if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
            // New service worker is ready
            console.log('New service worker available');
          }
        });
      });
    } catch (error) {
      console.log('Service Worker registration failed:', error);
    }
  });
}
