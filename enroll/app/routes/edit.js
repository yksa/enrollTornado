import Route from '@ember/routing/route';

export default class EditRoute extends Route {
    model(params){
        console.log(prarms);
        return this.store.findRecord('student', params.student_id);
    }
    // @action
    // updateInfo(student){
    //     student.save().then(() => this.transitionTo('list'));
    // }
}
