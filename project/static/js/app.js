(function(){
    var angular_module = angular.module('expenses_tracker', []);

    angular_module.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[{');
      $interpolateProvider.endSymbol('}]}');
    });

})();
