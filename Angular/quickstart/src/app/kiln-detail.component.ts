/**
 * Created by ThinkPad on 5/8/2017.
 */
import { Component, Input } from '@angular/core';
import { Kiln } from './kiln';



@Component({
  selector: 'kiln-detail',
  template: `
    <div *ngIf="kiln">
      <h2>{{kiln.name}} details!</h2>
      <div><label>id: </label>{{kiln.id}}</div>
      <div>
        <label>name: </label>
        <input [(ngModel)]="kiln.name" placeholder="name"/>
      </div>
    </div>
  `
})
export class KilnDetailComponent {
  @Input() kiln: Kiln;
}
