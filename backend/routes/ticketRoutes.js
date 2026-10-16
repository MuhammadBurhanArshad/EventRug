const express = require('express');
const { body, param } = require('express-validator');
const ticketController = require('../controllers/ticketController');
const validate = require('../middlewares/validate');

const router = express.Router();

const bookTicketValidation = [
  body('eventId').trim().notEmpty().withMessage('eventId is required to book a ticket'),
  body('attendeeName')
    .trim()
    .notEmpty()
    .withMessage('attendeeName is required')
    .isLength({ min: 2, max: 100 })
    .withMessage('attendeeName must be between 2 and 100 characters'),
  body('quantity')
    .optional()
    .isInt({ min: 1, max: 10 })
    .withMessage('Quantity must be an integer between 1 and 10'),
  body('tier').optional().trim(),
];

const checkInValidation = [
  param('code').trim().notEmpty().withMessage('Ticket code is required in URL parameter'),
  body('staffId').optional().trim(),
];

const wristbandValidation = [
  param('code').trim().notEmpty().withMessage('Ticket code is required in URL parameter'),
  body('wristbandId')
    .trim()
    .notEmpty()
    .withMessage('wristbandId is required')
    .isLength({ min: 3, max: 50 })
    .withMessage('wristbandId must be between 3 and 50 characters'),
];

router.post('/book', validate(bookTicketValidation), (req, res, next) =>
  ticketController.bookTicket(req, res, next)
);
router.get('/:id', (req, res, next) => ticketController.getTicketById(req, res, next));
router.get('/code/:code', (req, res, next) => ticketController.getTicketByCode(req, res, next));
router.post(
  '/code/:code/check-in',
  validate(checkInValidation),
  (req, res, next) => ticketController.checkInTicket(req, res, next)
);
router.post(
  '/code/:code/link-wristband',
  validate(wristbandValidation),
  (req, res, next) => ticketController.linkWristband(req, res, next)
);

module.exports = router;
