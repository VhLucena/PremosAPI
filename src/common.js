const status = require("http-status");

var exports = module.exports = {};
const fs = require('fs');

exports.crateInputFile = function(filename, request) {
    //console.log(request.params.metadata.algorithm);

    fs.writeFile(filename, JSON.stringify(request.body, replacer = null, space = 2), function(error){
        if(error) throw error;
        console.log('Input data saved sucessfully!');
    });
}

exports.ValidateInput = function(request) {
    return true;
}

exports.ErrorMessage = function(statusCode){
    var message = "";
    switch (statusCode) {
        case status.BAD_REQUEST:
            message = "Os dados de entrada não estão no formato correto.";
            break;
    
        default:
            message = "Ocorreu um erro inesperado.";
            break;
    }
    return message;
}

exports.ParserToString = function(data) {
    data = data.toString();
    var message = "";

    switch (data) {
        case "0":
            message = "Não";    
            break;
        
        case "1":
            message = "Sim";
            break;
    }

    return message
}