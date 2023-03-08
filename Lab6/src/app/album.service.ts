import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, map, Observable } from 'rxjs';
import { Album } from './album';
import { Photo } from './photo';
import { User } from './user';


@Injectable({
  providedIn: 'root'
})
export class AlbumService{
  private static apiUrl = "https://jsonplaceholder.typicode.com"

  constructor(private httpClient: HttpClient) {}

  getAlbums(): Observable<Album[]>{
    return this.httpClient.get<Album[]>(`${AlbumService.apiUrl}/albums`);
  }

  getAlbum(id: number): Observable<Album>{
    return this.httpClient.get<Album>(`${AlbumService.apiUrl}/albums/${id}`);
  }

  getUser(id: number): Observable<User>{
    return this.httpClient.get<User>(`${AlbumService.apiUrl}/users/${id}`);
  }

  deleteAlbum(id: number): Observable<Album>{
    return this.httpClient.delete<Album>(`${AlbumService.apiUrl}/albums/${id}`);
  }

  updateAlbum(album: Album){
    return this.httpClient.put<Album>(`${AlbumService.apiUrl}/albums/${album.id}`, album);
  }

  createAlbum(album: Album){
    return this.httpClient.post<Album>(`${AlbumService.apiUrl}/albums/${album.id}`, album);
  }

  getPhotos(albumId: number): Observable<Photo[]>{
    return this.httpClient.get<Photo[]>(`${AlbumService.apiUrl}/albums/${albumId}/photos`);
  }
}
