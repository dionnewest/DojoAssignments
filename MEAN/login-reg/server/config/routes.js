//imports
const Users = require('../controllers/users')
const Notes = require('../controllers/notes')
const path = require('path');

module.exports = function(app){
    app.post('/users', Users.create);
    app.post('/login', Users.authenticate);
    app.get('/session', Users.session);
    app.delete('/users', Users.logout);
    app.post('/notes', Notes.create);
    app.get('/notes', Notes.index);
    app.delete('/notes', Notes.delete);
    app.all('*', (req, res, next) => {
        res.sendFile(path.resolve('./public/dist/index.html'));
    });
} 