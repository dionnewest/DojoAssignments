const mongoose = require('mongoose');
const Task = mongoose.model('Task');

module.exports = {
    readAll(req, res){
        Task.find({}, function(err, task){
            if(err){
                return res.status(404).json(err);
            }
            return res.json(task)
        })
        res.json(true)
    },
    readOne(req, res){
        res.json(true)
    },
    create(req, res){
        res.json(true)
    },
    update(req, res){
        res.json(true)
    },
    destroy(req, res){
        res.json(true)
    }
}