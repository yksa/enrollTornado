import Route from '@ember/routing/route';

export default class DeleteRoute extends Route {
    model(params){
        return this.store.findRecord('student',params.student_id);
    }
}

