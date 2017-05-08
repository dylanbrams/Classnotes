import { Component } from '@angular/core';
import { Kiln } from './kiln';


const KILNS: Kiln[] = [
  { id: 11, name: 'Dylan\'s First Kiln'}
]

@Component({
  selector: 'my-app',
  template: `    
    <h1>{{title}}</h1>
    <h2>My Kilns</h2>
    <ul class="kilns">
      <li *ngFor="let current_kiln of kilns"
        [class.selected]="current_kiln === selectedKiln"
        (click)="onSelect(selectedKiln)">
        <span class="badge">{{current_kiln.id}}</span> {{current_kiln.name}}
      </li>
    </ul>
    <kiln-detail [kiln]="current_kiln"></kiln-detail>
    
  `,

  styles: [`
    .selected {
      background-color: #CFD8DC !important;
      color: white;
    }
    .kilns {
      margin: 0 0 2em 0;
      list-style-type: none;
      padding: 0;
      width: 15em;
    }
    .kilns li {
      cursor: pointer;
      position: relative;
      left: 0;
      background-color: #EEE;
      margin: .5em;
      padding: .3em 0;
      height: 1.6em;
      border-radius: 4px;
    }
    .kilns li.selected:hover {
      background-color: #BBD8DC !important;
      color: white;
    }
    .kilns li:hover {
      color: #607D8B;
      background-color: #DDD;
      left: .1em;
    }
    .kilns .text {
      position: relative;
      top: -3px;
    }
    .kilns .badge {
      display: inline-block;
      font-size: small;
      color: white;
      padding: 0.8em 0.7em 0 0.7em;
      background-color: #607D8B;
      line-height: 1em;
      position: relative;
      left: -1px;
      top: -4px;
      height: 1.8em;
      margin-right: .8em;
      border-radius: 4px 0 0 4px;
    }
  `]
})


export class AppComponent {
  title = 'Kiln Management List';
  kilns = KILNS;
  selectedKiln: Kiln;

  onSelectKiln(kiln: Kiln): void {
    this.selectedKiln = kiln;
  }
}



