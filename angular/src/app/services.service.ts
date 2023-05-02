import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  private UrlApi = 'http://192.168.0.11:8000';


  constructor(private http: HttpClient) { }

  getPacientes(): Observable<any> {
    return this.http.get(this.UrlApi +'/pacientes');
  }
}
