import { Component, OnInit} from '@angular/core';
import { Observable } from 'rxjs';
import { Album } from '../album';
import { AlbumService } from '../album.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit{
  albums: Album[] = [];
  
  constructor(private albumService: AlbumService){}

  ngOnInit(): void{
    this.albumService.getAlbums().subscribe((data) => {
      this.albums = data;
    })
  }

  deleteAlbum(id: number){
    this.albumService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter((album) => album.id !== id);
    })
  }

  createAlbum(title: string){
    let newAlbum: Album = {} as Album;
    newAlbum.title = title;
    this.albumService.createAlbum(newAlbum).subscribe(() => {
      this.albums.unshift(newAlbum)
    })
  }
}
