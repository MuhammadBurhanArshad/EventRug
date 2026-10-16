const express = require('express');
const healthRoutes = require('./healthRoutes');
const eventRoutes = require('./eventRoutes');
const ticketRoutes = require('./ticketRoutes');

const router = express.Router();

router.use('/health', healthRoutes);
router.use('/events', eventRoutes);
router.use('/tickets', ticketRoutes);

module.exports = router;
