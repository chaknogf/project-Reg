import { ServicesService } from './../../services.service';
import { Component, OnInit } from '@angular/core';
import { Ipacientes } from 'src/app/models/Ipaciente';

@Component({
  selector: 'pacientes',
  templateUrl: './pacientes.component.html',
  styleUrls: ['./pacientes.component.css']
})
export class PacientesComponent {

  public patient: Ipacientes[] = [];

  constructor(private ServicesService: ServicesService) { }

  ngOnInit() {
    this.ServicesService.getPacientes().subscribe((data) => {
      this.patient = data;
    });

  }
}
