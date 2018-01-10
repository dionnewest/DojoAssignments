import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { Note } from '../note';
import { NoteService } from '../note.service';



@Component({
  selector: 'app-note-new',
  templateUrl: './note-new.component.html',
  styleUrls: ['./note-new.component.css']
})
export class NoteNewComponent implements OnInit {

  @Output() createNoteEvent = new EventEmitter();

  newNote: Note = new Note;
  errors: string[] = [];
  constructor(private _ns: NoteService) { }

  ngOnInit() {
  }

  createNote() {
    console.log("Create Note Works Kinda")
    console.log(this.newNote)
    this._ns.create(this.newNote)
  }


}
