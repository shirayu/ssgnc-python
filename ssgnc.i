%module ssgnc
%include "std_string.i"
%include "stl.i"
%include "exception.i"
%include "ssgnc.h"

//----------------------------------
%{
    #include "ssgnc.h"
    using namespace ssgnc;
    using namespace std;

    class MyAgent {
        private:
            Agent *__agent;
            ssgnc::Int16 encoded_freq;
            std::vector<ssgnc::Int32> tokens;
        public:
            MyAgent(Agent *agent) : __agent(agent){
            };

            bool next(){
                return __agent->read(&encoded_freq, &tokens);
            };
            PyObject* getFreq(const Database &database){
                Int64 freq=0;
                if (!database.decodeFreq(encoded_freq, &freq)){
                    throw SWIG_RuntimeError;
                };
                return PyInt_FromLong(freq);
            };

            std::string getToken(const Database &database){
                ssgnc::StringBuilder ngram_str;
                if (!database.decodeTokens(tokens, &ngram_str))
                {
                    throw SWIG_RuntimeError;
                }
                return std::string(ngram_str.ptr());
            };
    };
%}
//----------------------------------

%exception{
    try{
        $action
    } catch (const std::exception &e){
        SWIG_exception(SWIG_RuntimeError, e.what() );
    } catch (...) {
        SWIG_exception(SWIG_UnknownError, "Unknown exception");
    }
}

//----------------------------------

namespace std {
    %template(IntVector) vector<int>;
    %template(IntMap) map<int, int>;
}

typedef int Int32;      
typedef long long Int64;

//----------------------------------

class Database {
    public:
        Database();
        ~Database();
        bool search(const Query &query, Agent *agent) const;
};

%extend Database{
    bool open(const char* path){
        return $self->open(path);
    }
    bool parseQuery(const char *str, Query *query) const{
        return $self->parseQuery(str, query);
    }
}

//----------------------------------

class Query {
    public:
        Query();
        ~Query();
};

%extend Query{
    bool parseKeyValue(const char* key, const char* value){
        return $self->parseKeyValue(String(key), String(value));
    }
}

//----------------------------------

class Agent {
    public:
        Agent();
        ~Agent();
};

//----------------------------------

class MyAgent {
    public:
        MyAgent(Agent *agent);
        ~MyAgent();
        bool next();
        PyObject* getFreq(const Database &database);
        std::string getToken(const Database &database);
};


