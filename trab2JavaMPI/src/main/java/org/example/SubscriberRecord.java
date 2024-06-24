package org.example;

import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.HashMap;

@Data
@Getter
@Setter
public class SubscriberRecord {
    HashMap<String, Integer> latestReadBySubject = new HashMap<>();
}
