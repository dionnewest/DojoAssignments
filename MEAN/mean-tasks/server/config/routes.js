const taskController = require('../controllers/tasks');

module.exports = function(app){
    app.get('/tasks', taskController.readAll);
    app.get('/tasks/:id', taskController.readOne);
    app.post('/tasks', taskController.create);
    app.put('/tasks/:id', taskController.update);
    app.delete('/tasks/:id'. taskController.destroy);
}