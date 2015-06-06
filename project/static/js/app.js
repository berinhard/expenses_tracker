(function(){
    var angular_module = angular.module('expenses_tracker', []);

    angular_module.config(function($interpolateProvider) {
      $interpolateProvider.startSymbol('{[{');
      $interpolateProvider.endSymbol('}]}');
    });

    angular_module.controller('expensesController', function($scope, $http){
        $http.get('https://lit-hollows-8740.herokuapp.com/expenses/')
        .success(function(data){
            $scope.expenses = data;
        })
    });
})();
