const helmet = require('helmet');
const cors = require('cors');
const hpp = require('hpp');
const rateLimit = require('express-rate-limit');
const config = require('../config');
const ApiResponse = require('../utils/apiResponse');

const rateLimiter = rateLimit({
  windowMs: config.rateLimit.windowMs,
  max: config.rateLimit.max,
  standardHeaders: true, // Return rate limit info in the `RateLimit-*` headers
  legacyHeaders: false, // Disable the `X-RateLimit-*` headers
  handler: (req, res) => {
    return ApiResponse.sendError(res, {
      statusCode: 429,
      message: 'Too many requests from this IP, please try again later.',
    });
  },
});

const securityMiddlewares = [
  // 1. Helmet for setting secure HTTP headers
  helmet({
    contentSecurityPolicy: {
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'"],
        styleSrc: ["'self'", "'unsafe-inline'"],
        imgSrc: ["'self'", 'data:', 'https:'],
      },
    },
    crossOriginEmbedderPolicy: false,
  }),

  // 2. CORS configuration
  cors({
    origin: config.cors.origin,
    methods: config.cors.methods,
    allowedHeaders: config.cors.allowedHeaders,
    credentials: true,
  }),

  // 3. HTTP Parameter Pollution protection
  hpp(),

  // 4. Rate Limiting for DoS protection
  rateLimiter,
];

module.exports = {
  securityMiddlewares,
  rateLimiter,
};
