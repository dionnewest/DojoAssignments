const mongoose = require('mongoose');
const Note = mongoose.model('Note');

class NotesController{
    create(req, res){
        Note.create(req.body, (err, note) =>{
            if(err){
                return res.json(err)
            } else {
                return res.json(note);
            }
        })
    }
    index(req, res){
        Note.find({}).sort('-createdAt').exec((err, notes) => {
            if(err){
                return res.json(err)
            } else {
                return res.json(notes)
            }
        })
    }
    delete(req, res){
        Note.remove({}, (err, note) =>{
            if (err) {
                return res.json(err)
            } else {
                return res.json(note);
            }
        })
    }
}

module.exports = new NotesController();