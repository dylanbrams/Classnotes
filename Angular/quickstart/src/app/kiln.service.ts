/**
 * Created by ThinkPad on 5/8/2017.
 */
import { Injectable } from '@angular/core';
import { Headers, Http, HttpModule } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import { Kiln } from './kiln';
// import { KILNS } from './testdata/offline_kilns';


@Injectable()
export class KilnService {
  private kilnsUrl = 'http://localhost:8000/api/kiln/';  // URL to web api
  mystr = {str: 'test'};
  constructor (private http: Http) {}
  getKilns(): Promise<Kiln[]> {
    return this.http.get(this.kilnsUrl, JSON.stringify(this.mystr))
      .toPromise()
      .then(response => response.json().data as Kiln[])
      .catch (this.handleError);
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
  getKiln(id: number): Promise<Kiln> {
  return this.getKilns()
             .then(kilns => kilns.find(kiln => kiln.id === id));
  }
}
