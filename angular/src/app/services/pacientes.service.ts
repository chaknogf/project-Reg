import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Ipaciente } from '../models/ipaciente';

@Injectable({
  providedIn: 'root'
})
export class PacientesService {
  private urlapi = "http://localhost:8000";
  constructor(private http: HttpClient) { }

  getPacientes(): Observable<any>{
    return this.http.get(this.urlapi + "/pacientes");
  }

  getPaciente(exp: number): Observable<any>{
    return this.http.get(this.urlapi + "/pacientes/" + exp);
  }

  crearPaciente(paciente: Ipaciente): Observable<any>{
    return this.http.post(this.urlapi + "/pacientes", paciente);
  }

  editPaciente(exp: number, updateP: Ipaciente): Observable<any>{
    return this.http.put(this.urlapi + "/pacientes/" + exp, updateP);
  }

  deletePaciente(exp: number): Observable<any>{
    return this.http.delete(this.urlapi + "/pacientes/" + exp);
  }







}
