const { Pool } = require('pg');
const config = require('./index');

let pool = null;

if (process.env.DATABASE_URL) {
  pool = new Pool({
    connectionString: process.env.DATABASE_URL,
    ssl: process.env.NODE_ENV === 'production' ? { rejectUnauthorized: false } : false,
    max: 20, // Max concurrent connections
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 2000,
  });

  pool.on('error', (err) => {
    console.error('[EventRug Database] Unexpected PostgreSQL pool error', err);
  });
}

/**
 * Execute a query with connection pooling
 * @param {string} text - SQL query
 * @param {Array} params - Query parameters
 */
const query = async (text, params) => {
  if (!pool) {
    throw new Error('DATABASE_URL is not configured. Provide connection string in .env');
  }
  const start = Date.now();
  const res = await pool.query(text, params);
  const duration = Date.now() - start;
  if (config.env === 'development') {
    console.log('[PostgreSQL Executed Query]', { text, duration: `${duration}ms`, rows: res.rowCount });
  }
  return res;
};

module.exports = {
  pool,
  query,
};
