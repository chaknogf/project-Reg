import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'numberToText'
})
export class NumberToTextPipe implements PipeTransform {
  transform(value: number): string {
    // Convierte el número en texto según tu lógica de formato
    const stringValue = value.toString();
    const formattedValue = stringValue.replace(/(\d{4})(\d{5})(\d{4})/, '$1 $2 $3');
    return formattedValue;
  }
}
