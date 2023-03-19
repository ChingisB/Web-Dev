import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { switchMap } from 'rxjs';
import { Album } from '../album';
import { AlbumService } from '../album.service';
import { User } from '../user';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit{
  album!: Album;
  user: User = new User({
    id: 0, name: "", username: "", email: "",
    address: {}, phone: "", website: "", company: {}
  });
  id: number = 0;

  constructor(private route: ActivatedRoute, private albumService: AlbumService, private location: Location){}

  ngOnInit(): void {
    this.route.paramMap.pipe(
      switchMap(params => {
        this.id = Number(params.get('id'));
        return this.albumService.getAlbum(this.id);
      }),
      switchMap(album => {
        this.album = album;
        return this.albumService.getUser(this.album.userId);
      })
    ).subscribe(user => {
      this.user = user;
    });
  }

  backOnClick(){
    this.location.back(); 
  }

  saveOnClick(newTitle: string){
    this.album.title = newTitle;
    this.albumService.updateAlbum(this.album).subscribe((newAlbum) => {
      this.album = newAlbum;
    })
  }
}
