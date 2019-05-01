const common = require('../common');
const status = require("http-status");
const { spawn } = require('child_process');


exports.getPrediction = (request, response, next) => {
  //const id = request.params.id;
  
  var valid = common.ValidateInput(request);
  
  if(!valid) {
    response.status(status.BAD_REQUEST);
    var message = common.ErrorMessage(status.BAD_REQUEST);
    response.send(message);
    return;
  } 

  filename = 'input.json'
  path = 'input/' + filename;
    
  common.crateInputFile(path, request);
  
  const pythonModel = spawn('python', ['python_models/PredictorController.py', filename]);

  pythonModel.stdout.on('data', function(data) {
    response.send(data.toString());
  });
};
