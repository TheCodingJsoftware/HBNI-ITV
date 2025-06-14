from dataclasses import dataclass
from app.curiki.cluster import Cluster
from app.curiki.general_learning_outcome import GeneralLearningOutcome
from app.curiki.learning_type import LearningType
from app.curiki.outcome import Outcome


@dataclass(frozen=True)
class SocialStudiesOutcome(Outcome):
    cluster: Cluster
    outcome_type: LearningType
    general_learning_outcome: GeneralLearningOutcome  # These are letter codescode
    distinctive_learning_outcome: LearningType  # These are letter codes

    def to_dict(self) -> dict:
        return {
            "outcome_id": self.outcome_id,
            "grade": self.grade,
            "cluster": self.cluster.to_dict(),
            "outcome_type": self.outcome_type.to_dict(),
            "general_learning_outcome": self.general_learning_outcome.to_dict(),
            "distinctive_learning_outcome": self.distinctive_learning_outcome.to_dict(),
        }
