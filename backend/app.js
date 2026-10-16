const express = require('express');
const compression = require('compression');
const morgan = require('morgan');
const cookieParser = require('cookie-parser');
const config = require('./config');
const { securityMiddlewares } = require('./middlewares/security');
const { generateCsrfToken } = require('./middlewares/csrf');
const notFoundHandler = require('./middlewares/notFound');
const errorHandler = require('./middlewares/errorHandler');
const apiRoutes = require('./routes');
const ApiResponse = require('./utils/apiResponse');

const app = express();

// 1. Trust proxy headers (useful when deployed behind Nginx, Cloudflare, etc.)
app.set('trust proxy', 1);

// 2. Request logger
if (config.env !== 'test') {
  app.use(morgan(config.env === 'development' ? 'dev' : 'combined'));
}

// 3. Security Middlewares (Helmet, CORS, HPP, Rate Limiting)
app.use(securityMiddlewares);

// 4. Request Body and Cookie Parsers
app.use(cookieParser());
app.use(express.json({ limit: config.bodyLimit }));
app.use(express.urlencoded({ extended: true, limit: config.bodyLimit }));

// 5. Response compression
app.use(compression());

// 6. Base Root & CSRF Token Endpoints
app.get('/', (req, res) => {
  return ApiResponse.sendSuccess(res, {
    message: 'EventRug REST API is running',
    data: {
      version: '1.0.0',
      docs: `${config.apiPrefix}/health`,
    },
  });
});

app.get('/csrf-token', (req, res) => {
  const token = generateCsrfToken(req, res);
  return ApiResponse.sendSuccess(res, {
    message: 'CSRF token generated',
    data: { csrfToken: token },
  });
});

// 7. REST API routes
app.use(config.apiPrefix, apiRoutes);

// 8. 404 Handler
app.use(notFoundHandler);

// 9. Centralized Error Handler
app.use(errorHandler);

module.exports = app;
