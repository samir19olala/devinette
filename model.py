

class Question:
    """_summary_ class question est une classe
        qui va implementer nos questions
        champs:
                nombre_question( variablede classe)
                self.__titre = titre
                self.__propositions = propositions
                self.__reponse = reponse
        methodes

        et une variable de classe nombre_question
    """
    nombre_question = 0
    
    def __init__(self,titre:str,propositions:list[str],reponse:str)->None:
        
        Question.nombre_question+=1
        
        self.id_question = Question.nombre_question
        self.titre = titre
        self.propositions = propositions
        self.reponse = reponse
        
        


# creation de la classe questionnaire 


class Questionnaire:
    """_summary_ class Questionnaire 
        c'est la classe qui va organiser nos questions
        __champs :

        nombre_questionnaire (variable de classe)
        self.id_questionnaire
        self.niveau = niveau
        self.questions = questions
        
    """
    nombre_questionnaire = 0
    
    def __init__(self ,niveau:str,questions :list[Question]) ->None:       
        
        Questionnaire.nombre_questionnaire+=1
        self.id_questionnaire = Questionnaire.nombre_questionnaire
        self.niveau = niveau
        self.questions = questions
        
        
        