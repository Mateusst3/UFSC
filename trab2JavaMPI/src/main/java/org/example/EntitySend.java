package org.example;

public class EntitySend {

    private String interest;
    private String message;

    public EntitySend(String interest, String message) {
        this.interest = interest;
        this.message = message;
    }

    public String getInterest() {
        return interest;
    }

    public void setInterest(String interest) {
        this.interest = interest;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
