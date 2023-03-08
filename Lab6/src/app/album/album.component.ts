import { HttpClient } from '@angular/common/http';
import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { Album } from '../album';
import { AlbumService } from '../album.service';
import { User } from '../user';

@Component({
  selector: 'app-album',
  templateUrl: './album.component.html',
  styleUrls: ['./album.component.css']
})
export class AlbumComponent implements OnInit {
  @Input() album: Album = { userId: 0, id: 0, title: "" };
  @Output() deleteAlbum = new EventEmitter<number>();
  user: User = new User({
    id: 0, name: "", username: "", email: "",
    address: {}, phone: "", website: "", company: {}
  });

  constructor(private albumService: AlbumService) { }

  ngOnInit(): void {
    this.albumService.getUser(this.album.userId).subscribe((data) => {
      this.user = data;
    })
  }

  delete(): void {
    this.deleteAlbum.emit(this.album.id);
  }
}
