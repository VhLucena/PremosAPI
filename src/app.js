const http = require("http");
const express = require("express");
const status = require("http-status");
const premosRoute = require("./routes/PremosRoutes.js");

const { spawn } = require('child_process');

const app = express();

app.use(express.json());

app.use("/premos", premosRoute);

app.get('/', (req, res) => {
    res.send('Server Running');
});

app.use((request, response, next) => {
    response.status(status.NOT_FOUND).send();
});


app.listen(9090, function(){
    console.log('Server running at 9090');
});

