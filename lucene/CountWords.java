/**
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * 
 * Author: Ricard Gavalda, http://www.lsi.upc.edu/gavalda
 * Initial date (for version 3.6.x): April 10th, 2012
 * Ported to version 4.x: September 19th, 2014; tested on 4.7.1 and 4.10.0
 * Based on the org.lucene.demo.SearchFiles class
 */

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Date;

//import org.apache.lucene.analysis.Analyzer;
//import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.SlowCompositeReaderWrapper;
import org.apache.lucene.index.Fields;
import org.apache.lucene.index.Terms;
//import org.apache.lucene.index.TermDocs;
import org.apache.lucene.index.TermsEnum;
import org.apache.lucene.index.SingleTermsEnum;
import org.apache.lucene.index.Term;
import org.apache.lucene.store.FSDirectory;
//import org.apache.lucene.util.Version;

/* Open an index given as argument, and print to standard output
 * all the terms contained in its "contents" field, together with their
 * total count (not document count, but total number of occurrences 
 * in the indexed document collection). Order as provided by the index */
public class CountWords {

  private CountWords() {}

  public static void main(String[] args) throws Exception {

    if (args.length != 1) {
       String usage = "Usage:\tjava CountWords indexdir";
       System.out.println(usage);
       System.exit(0);
    }

    String index = args[0];
    // String field = "contents";
    String queries = null;
        
    IndexReader reader = DirectoryReader.open(FSDirectory.open(new File(index)));
    Terms terms = SlowCompositeReaderWrapper.wrap(reader).terms("contents");
    TermsEnum tenum = terms.iterator(null);
    long totalOccs = 0;
    long i = 0;
    while (i < terms.size()) {
		long n = tenum.totalTermFreq();
		totalOccs += n;
        System.out.println(tenum.term().utf8ToString()+" "+n);
        tenum.next();
        ++i;
    }
    System.out.println("Distinct words: "+i+"; Word occurrences: "+totalOccs);
  }
}
