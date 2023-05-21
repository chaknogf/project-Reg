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

  getPaciente(exp: number) {
    this.pacientesService.getPaciente(exp).subscribe(data => {
      this.pacientes = data;
      });
  }




  calcularEdad(Nacimiento: Date) {
    const hoy = new Date();
    const fechaNac = new Date(Nacimiento);
    let años = hoy.getFullYear() - fechaNac.getFullYear();
    let meses = hoy.getMonth() - fechaNac.getMonth();
    let dias = hoy.getDate() - fechaNac.getDate();
    if (meses < 0 || (meses === 0 && dias < 0)) {
      años--;
      meses += 12;
      if (dias < 0) {
        meses--;
        dias += new Date(hoy.getFullYear(), hoy.getMonth(), 0).getDate();
      }
    } else if (dias < 0) {
      meses--;
      dias += new Date(hoy.getFullYear(), hoy.getMonth(), 0).getDate();
    }

    return `${años}a ${meses}m ${dias}d`;
  }



}




