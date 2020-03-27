import Route from '@ember/routing/route';

export default class ListRoute extends Route {
    model(){
        const student = this.store.findAll('student');
        return {student};
    }
}
