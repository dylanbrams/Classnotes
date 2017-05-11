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
  private kilnsUrl = 'http://localhost:8000/api/kilnpublic/';  // URL to web api
  mystr = {str: 'test'};
  constructor (private http: Http) {}
  getKilns(): Promise<Kiln[]> {
    let kilnsData = this.http.get(this.kilnsUrl, JSON.stringify(this.mystr))
      .toPromise()
      .then(response => response.json().results as Object[])
      .catch (this.handleError);
    return kilnsData;
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }
  getKiln(kiln_id: number): Promise<Kiln> {
  let kilnData = this.getKilns()
             .then(kilns => kilns.find(kiln => kiln.kiln_id === kiln_id));
  return kilnData;
  }
}
