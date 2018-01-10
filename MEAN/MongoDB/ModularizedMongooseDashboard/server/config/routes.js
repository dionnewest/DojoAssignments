var mongeese = require('../controllers/mongeese.js');
module.exports = function(app) {
  app.get('/', mongeese.show) //Read
  app.post('/mongeese', mongeese.create) //Create
  app.post ('/mongeese/:id', mongeese.update) //Update
  app.get('/mongeese/:id', mongeese.profile) //View profile of selected mongoose
  app.get('/mongeese/edit/:id', mongeese.edit)
  app.get('/mongeese/destroy/:id', mongeese.destroy)
  app.get('/new', mongeese.new)
}

