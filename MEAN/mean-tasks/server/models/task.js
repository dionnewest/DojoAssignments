const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const TaskSchema = new Schema({
    content:{
        type: String,
        required: [true, 'content is required'],
        minlength: [5, 'content must be at least 5 characters long']
    },
    asignee:{
        name:{
            type: String
        },
        status:{
            type: Boolean
        }
    }
}, {timestamps: true})

mongoose.model('Task', TaskSchema);