<!--{% block content %}-->
<!--    <div class="container">-->
<!--        <form action="/student" method="post">-->
<!--            {% csrf_token %}-->
<!--            <div class="col-md-8 col-md-offset-2">-->
<!--                <div class="panel panel-default">-->
<!--                    <div class="panel-heading">Register</div>-->
<!--                    <div class="panel-body">-->
<!--                        {% if error_message %}-->
<!--                            <p class="bg-danger p-d ml-b">{{ error_message }}</p>-->
<!--                        {% endif %}-->

<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.name.id_for_label }}" class="col-md-4 control-label text-right">Username<span class="text-red">*</span>:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.name }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.dob.id_for_label }}" class="col-md-4 control-label text-right">Email<span class="text-red">*</span>:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.dob }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.age.id_for_label }}" class="col-md-4 control-label text-right">Password<span class="text-red">*</span>:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.age }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.gender.id_for_label }}" class="col-md-4 control-label text-right">Confirm password:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.gender }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.phn_no.id_for_label }}" class="col-md-4 control-label text-right">Phone No:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.phn_no }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.email.id_for_label }}" class="col-md-4 control-label text-right">Email Id:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.email }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="form-group clearfix">-->
<!--                            <label for="{{ form.address.id_for_label }}" class="col-md-4 control-label text-right">Address:</label>-->
<!--                            <div class="col-md-6">-->
<!--                                {{ form.address }}-->
<!--                            </div>-->
<!--                        </div>-->
<!--                        <div class="col-md-6 col-md-offset-4">-->
<!--                            <input type="submit" value="Submit" class="btn btn-success">-->
<!--                        </div>-->
<!--                    </div>-->
<!--                </div>-->
<!--            </div>-->
<!--        </form>-->
<!--    </div>-->