import { Component, OnInit } from '@angular/core';
import { PacientesService } from 'src/app/services/pacientes.service';
import { Ipaciente } from 'src/app/models/ipaciente';
@Component({
  selector: 'pacientes',
  templateUrl: './pacientes.component.html',
  styleUrls: ['./pacientes.component.css']
})
export class PacientesComponent{
  public pacientes: Ipaciente[] = [];

  constructor(private pacientesService: PacientesService) { }

  ngOnInit(){
    this.pacientesService.getPacientes().subscribe(data => {
      this.pacientes = data;
    })
  }

  delete(exp: number) {
    this.pacientesService.deletePaciente(exp).subscribe(data => {
      this.pacientes = data;
      this.ngOnInit();
    });
  }



}

