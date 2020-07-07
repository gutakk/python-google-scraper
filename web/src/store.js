import { observable } from 'mobx';

class store {
    @observable register = {
        username: null,
        password: null,
        confirmPassword: null
    }
}

const store = new store();
export default store;