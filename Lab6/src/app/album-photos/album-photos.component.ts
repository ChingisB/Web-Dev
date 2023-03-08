import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumService } from '../album.service';
import { Photo } from '../photo';
import { Location } from '@angular/common';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit{
  id: number = 0;
  photos: Photo[] = [];

  constructor(private albumService: AlbumService, private route: ActivatedRoute,
              private location: Location){}

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      this.id = Number(params.get("id"));
    })
    this.albumService.getPhotos(this.id).subscribe((photos) => {
      this.photos = photos;
    })
  }

  backOnClick(){
    this.location.back(); 
  }
}
