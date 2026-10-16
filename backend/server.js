const app = require('./app');
const config = require('./config');

const server = app.listen(config.port, () => {
  console.log(`[EventRug API] Server listening on port ${config.port} (${config.env})`);
  console.log(`[EventRug API] API Base URL: http://localhost:${config.port}${config.apiPrefix}`);
});

// Graceful shutdown
const handleShutdown = (signal) => {
  console.log(`\n[EventRug API] Received ${signal}. Gracefully shutting down...`);
  server.close(() => {
    console.log('[EventRug API] HTTP server closed.');
    process.exit(0);
  });

  // Force close after 10s
  setTimeout(() => {
    console.error('[EventRug API] Could not close connections in time, forcefully shutting down');
    process.exit(1);
  }, 10000);
};

process.on('SIGTERM', () => handleShutdown('SIGTERM'));
process.on('SIGINT', () => handleShutdown('SIGINT'));

module.exports = server;
