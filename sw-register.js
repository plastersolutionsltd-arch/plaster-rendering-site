/**
 * Service Worker — actively unregister any existing registrations.
 * The site is served from Vercel CDN; no SW needed.
 */
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then((registrations) => {
    for (const reg of registrations) {
      reg.unregister();
    }
  });
}
