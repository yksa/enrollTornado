import EmberRouter from '@ember/routing/router';
import config from './config/environment';

export default class Router extends EmberRouter {
  location = config.locationType;
  rootURL = config.rootURL;
}

Router.map(function() {
  this.route('list');
  this.route('edit',{path: '/edit/:student_id'});
  this.route('delete');
});
