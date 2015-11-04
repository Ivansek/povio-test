var blogController = angular.module('blogControllers', [])

blogController.controller('IndexController', function($scope, $http){
    var list_all = function(){
        $http.get('/api/post').success(function(data){
            $scope.posts = data

        })

    }
    $scope.delete = function(post){
        var sure = confirm('Are you sure you want to delete this post?')
        if( sure ) {
            $http.delete('/api/post/' + post.id, post);
            var index = $scope.posts.indexOf(post)
            $scope.posts.splice(index, 1)
        }
    }
    list_all()
})

blogController.controller('NewPostController', function($scope, $http){
    $scope.formData = {}
    $scope.processForm = function(){
        $http.post('/api/post/', $scope.formData)
            .success(function(data){
                $scope.is_error = false
                $scope.submitted = true
                $scope.status = 'Your post was successfully saved!'
                $scope.formData = {}
            })
            .error(function(data){
                $scope.submitted = true
                $scope.is_error = true
                $scope.errors = data
            })
    }
})
//
////blogController.directive("remove", function () {
//    return function (scope, element, attrs) {
//        element.bind ("mousedown", function () {
//            scope.remove(element);
//            scope.$apply();
//        })
//    };
//
//});
