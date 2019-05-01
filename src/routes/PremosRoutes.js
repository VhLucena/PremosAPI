const express = require('express');
const controller = require('../controller/PremosController');

const router = express.Router();

router.get('/predict', controller.getPrediction);

module.exports = router;