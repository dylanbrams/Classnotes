"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require("@angular/core");
var kiln_service_1 = require("./kiln.service");
var router_1 = require("@angular/router");
var KilnsComponent = (function () {
    function KilnsComponent(kilnService, router) {
        this.kilnService = kilnService;
        this.router = router;
        this.title = 'Kiln Management List';
    }
    KilnsComponent.prototype.getKilns = function () {
        var _this = this;
        this.kilnService.getKilns()
            .then(function (kilns) { return _this.kilns = kilns; });
    };
    KilnsComponent.prototype.ngOnInit = function () {
        this.getKilns();
    };
    KilnsComponent.prototype.onSelectKiln = function (kiln) {
        this.selectedKiln = kiln;
    };
    KilnsComponent.prototype.gotoDetail = function () {
        this.router.navigate(['/detail', this.selectedKiln.id]);
    };
    return KilnsComponent;
}());
KilnsComponent = __decorate([
    core_1.Component({
        selector: 'my-kilns',
        templateUrl: "./kilns.component.html",
        styleUrls: ["./kilns.component.css"]
    }),
    __metadata("design:paramtypes", [kiln_service_1.KilnService, router_1.Router])
], KilnsComponent);
exports.KilnsComponent = KilnsComponent;
//# sourceMappingURL=kilns.component.js.map