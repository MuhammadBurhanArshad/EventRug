const express = require('express');
const { body, param, query } = require('express-validator');
const eventController = require('../controllers/eventController');
const validate = require('../middlewares/validate');

const router = express.Router();

const createEventValidation = [
  body('title')
    .trim()
    .notEmpty()
    .withMessage('Event title is required')
    .isLength({ min: 3, max: 150 })
    .withMessage('Title must be between 3 and 150 characters'),
  body('venue').trim().notEmpty().withMessage('Event venue is required'),
  body('date')
    .notEmpty()
    .withMessage('Event date is required')
    .isISO8601()
    .withMessage('Date must be a valid ISO 8601 date string'),
  body('totalCapacity')
    .notEmpty()
    .withMessage('Total capacity is required')
    .isInt({ min: 1 })
    .withMessage('Total capacity must be an integer greater than 0'),
  body('price')
    .optional()
    .isFloat({ min: 0 })
    .withMessage('Price must be a non-negative number'),
  body('category').optional().trim(),
  body('description').optional().trim(),
];

const updateEventValidation = [
  param('id').notEmpty().withMessage('Event ID parameter is required'),
  body('title').optional().trim().isLength({ min: 3, max: 150 }),
  body('totalCapacity').optional().isInt({ min: 1 }),
  body('price').optional().isFloat({ min: 0 }),
];

router.get('/', (req, res, next) => eventController.getEvents(req, res, next));
router.get('/:id', (req, res, next) => eventController.getEventById(req, res, next));
router.post('/', validate(createEventValidation), (req, res, next) =>
  eventController.createEvent(req, res, next)
);
router.patch('/:id', validate(updateEventValidation), (req, res, next) =>
  eventController.updateEvent(req, res, next)
);
router.delete('/:id', (req, res, next) => eventController.deleteEvent(req, res, next));

module.exports = router;
