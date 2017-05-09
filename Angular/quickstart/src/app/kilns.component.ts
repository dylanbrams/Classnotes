import { Component, OnInit } from '@angular/core';
import { Kiln } from './kiln';
import { KilnService }         from './kiln.service';
import { Router } from '@angular/router';

@Component({
  selector: 'my-kilns',
  templateUrl: `./kilns.component.html`,
  styleUrls: [`./kilns.component.css`]
})


export class KilnsComponent implements OnInit {
  title = 'Kiln Management List';
  kilns: Kiln[];
  selectedKiln: Kiln;

  constructor(private kilnService: KilnService, private router: Router) { }
  getKilns(): void {
    this.kilnService.getKilns()
      .then(kilns => this.kilns = kilns);
  }
  ngOnInit(): void {
    this.getKilns();
  }
  onSelectKiln(kiln: Kiln): void {
    this.selectedKiln = kiln;
  }
  gotoDetail(): void {
    this.router.navigate(['/detail', this.selectedKiln.id]);
}
}



