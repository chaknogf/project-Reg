import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'formatoDPI'
})
export class FormatoDPIPipe implements PipeTransform {
  transform(value: string): string {
    const firstFourDigits = value.substr(0, 4);
    const nextFiveDigits = value.substr(4, 6);
    const remainingDigits = value.substr(10);
    const formattedValue = `${firstFourDigits} ${nextFiveDigits} ${remainingDigits}`;
    return formattedValue.trim(); // Elimina espacios adicionales al inicio y al final
  }


}
