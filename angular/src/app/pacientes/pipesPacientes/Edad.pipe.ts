import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'edad'
})
export class EdadPipe implements PipeTransform {
  transform(nacimiento: Date): string {
    const hoy = new Date();
    const fechaNac = new Date(nacimiento);
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

    return `${años} años ${meses} meses ${dias} días`;
  }
}
